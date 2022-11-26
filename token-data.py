import json
import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 10000):
    with open(f"./tokens/{i}.json", "w") as f:
        f.write(
            json.dumps(
                {
                    "attributes": [
                        {
                            "trait_type": "Number",
                            "value": f"{i}",
                        },
                        {
                            "trait_type": "Prime",
                            "value": f"{is_prime(i)}",
                        },
                    ],
                    "description": "Numbers collection",
                    "image": f"https://raw.githubusercontent.com/Naranbayar/sample-nft-data/master/images/{i}.png",
                    "name": f"Number #{i}",
                }
            )
        )
