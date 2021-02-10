from .constants import compute_sha256_constants
from .fixed_size_int import FixedSizeInt
from .utils import choice, majority, sigma0, sigma1, Sigma0, Sigma1

CONSTANTS, INITIAL_WORKING_VARIABLES = compute_sha256_constants()


def build_message_blocks(byte_stream, block_size=512):
    raw_message = "".join([FixedSizeInt(b, n_bits=8).bin() for b in byte_stream])

    # Format message with 0-padding and message length
    message_length = FixedSizeInt(len(raw_message), n_bits=64)
    padding_length = -(message_length.value + 1 + 64) % block_size
    formatted_message = raw_message + "1" + "0" * padding_length + message_length.bin()
    assert len(formatted_message) % block_size == 0

    # Yield blocks of 512 bits
    for i in range(0, len(formatted_message), block_size):
        yield formatted_message[i: i + block_size]


def build_block_schedule(block):
    assert (len(block) == 512)
    schedule = []
    for t in range(64):
        if t < 16:
            word_b = block[t * 32: (t + 1) * 32]
            word = FixedSizeInt(int(word_b, base=2), n_bits=32)
        else:
            word = sigma1(schedule[t - 2]) + schedule[t - 7] + sigma0(schedule[t - 15]) + schedule[t - 16]
        schedule.append(word)
    return schedule


def compress_block(block, initial_working_variables):
    schedule = build_block_schedule(block)
    a, b, c, d, e, f, g, h = initial_working_variables

    for word, constant, in zip(schedule, CONSTANTS):
        t1 = Sigma1(e) + choice(e, f, g) + h + constant + word
        t2 = Sigma0(a) + majority(a, b, c)
        b, c, d, e, f, g, h = a, b, c, d, e, f, g
        a = t1 + t2
        e += t1

    # Add current working variables with initial ones
    a += initial_working_variables[0]
    b += initial_working_variables[1]
    c += initial_working_variables[2]
    d += initial_working_variables[3]
    e += initial_working_variables[4]
    f += initial_working_variables[5]
    g += initial_working_variables[6]
    h += initial_working_variables[7]

    return a, b, c, d, e, f, g, h


def hash_byte_stream(byte_stream):
    assert isinstance(byte_stream, bytearray) or isinstance(byte_stream, bytes)

    # Split the byte_stream in blocks
    blocks = build_message_blocks(byte_stream)

    # Compress blocks recursively
    working_variables = INITIAL_WORKING_VARIABLES
    for block in blocks:
        working_variables = compress_block(block, working_variables)

    # Concatenate the working variables to get the final hash
    hash_value = "".join([x.bin() for x in working_variables])
    assert len(hash_value) == 256
    return FixedSizeInt(int(hash_value, base=2), 256)

