'''
This program is a implementation of MD2 hash function algotihm

REFERENCES
    - Medium: https://nickthecrypt.medium.com/cryptography-hash-method-md2-message-digest-2-step-by-step-explanation-made-easy-with-python-10faa2e35e85
    - RFC: https://tools.ietf.org/html/rfc1319

INTRO
Four Steps to obtain the hash signature:
    - Step 1 - Padding the message
    - Step 2 - Append checksum
    - Step 3 - Initialize digest
    - Step 4 - Process the message in 16-bytes blocks
'''

string = "After killing\r\na spider, how lonely I feel\r\nin the cold of night!"

msg = [ord(c) for c in string]

# Step 0 - Define constants


BLOCK_SIZE = 16


S = [
    41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6, 19,
    98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188, 76, 130, 202,
    30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24, 138, 23, 229, 18,
    190, 78, 196, 214, 218, 158, 222, 73, 160, 251, 245, 142, 187, 47, 238, 122,
    169, 104, 121, 145, 21, 178, 7, 63, 148, 194, 16, 137, 11, 34, 95, 33,
    128, 127, 93, 154, 90, 144, 50, 39, 53, 62, 204, 231, 191, 247, 151, 3,
    255, 25, 48, 179, 72, 165, 181, 209, 215, 94, 146, 42, 172, 86, 170, 198,
    79, 184, 56, 210, 150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241,
    69, 157, 112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2,
    27, 96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
    85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197, 234, 38,
    44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65, 129, 77, 82,
    106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123, 8, 12, 189, 177, 74,
    120, 136, 149, 139, 227, 99, 232, 109, 233, 203, 213, 254, 59, 0, 29, 57,
    242, 239, 183, 14, 102, 88, 208, 228, 166, 119, 114, 248, 235, 117, 75, 10,
    49, 68, 80, 180, 143, 237, 31, 26, 219, 153, 141, 51, 159, 17, 131, 20
]

# Step 1 - Padding the message
padding_len = BLOCK_SIZE - (len(msg) % BLOCK_SIZE)
padding = padding_len * [padding_len]
msg += padding

N = len(msg)
BLOCKS_COUNT = N // BLOCK_SIZE


# Step 2 - Append checksum
checksum = BLOCK_SIZE * [0]
l = 0

for i in range(BLOCKS_COUNT):
    for j in range(BLOCK_SIZE):
        l = S[msg[i * BLOCK_SIZE + j] ^ l] ^ checksum [j]
        checksum[j] = l

msg += checksum
BLOCKS_COUNT += 1


# Step 3 - Initialize digest
digest = 48 * [0]
CHUNK_0 = 0
CHUNK_1 = BLOCK_SIZE
CHUNK_2 = 2 * BLOCK_SIZE

for i in range(BLOCKS_COUNT):
    for j in range(BLOCK_SIZE):
        digest[CHUNK_1 + j] = msg[i * BLOCK_SIZE + j]
        digest[CHUNK_2 + j] = digest[CHUNK_1 + j] ^ digest [j]
        
        check_tmp = 0

    for j in range(18):
        for k in range(48):
            check_tmp = digest[k] ^ S[check_tmp]
            digest[k] = check_tmp
        check_tmp = (check_tmp + j) % 256


# Step 4 - Process the message in 16-bytes blocks
for x in digest[0:16]:
    # print(hex(x))
    print(hex(x).lstrip("0x"), end='')