import unittest

from pysha256.constants import compute_sha256_constants
from pysha256.hash import build_block_schedule, build_message_blocks, compress_block, hash_byte_stream


class TestHash(unittest.TestCase):

    def test_build_message_blocks(self):
        byte_stream = bytearray([97, 98, 99])

        # Size 512
        blocks = list(build_message_blocks(byte_stream, block_size=512))
        self.assertEqual(len(blocks), 1)
        block = blocks[0]
        self.assertEqual(int(block[-64:], base=2), 24)  # Message length (encoded on the last 64 bits)
        self.assertEqual(block[24], '1')
        self.assertTrue(all([x == '0' for x in block[25:-64]]))
        self.assertEqual(int(block[8:16], base=2), 98)

        # Size 64
        blocks = list(build_message_blocks(byte_stream, block_size=64))
        self.assertEqual(len(blocks), 2)
        self.assertEqual(int(blocks[1], base=2), 24)
        self.assertEqual(blocks[0][24:], "1" + "0" * 39)

    def test_build_block_schedule(self):
        block = "01100001011000100110001110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000"
        schedule = build_block_schedule(block)
        self.assertEqual(len(schedule), 64)
        self.assertEqual(schedule[0], 1633837952)
        self.assertEqual(schedule[63], 313650667)

    def test_compress_block(self):
        block = "01100001011000100110001110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000"
        _, initial_working_variables = compute_sha256_constants()
        a, b, c, d, e, f, g, h = compress_block(block, initial_working_variables)
        self.assertEqual(a, 3128432319)
        self.assertEqual(b, 2399260650)
        self.assertEqual(c, 1094795486)
        self.assertEqual(d, 1571693091)

    def test_hash_byte_stream(self):
        byte_stream = bytearray([97, 98, 99])
        hash_value = hash_byte_stream(byte_stream)
        good_hash = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        self.assertEqual(hash_value, int(good_hash, base=16))


if __name__ == '__main__':
    unittest.main()
