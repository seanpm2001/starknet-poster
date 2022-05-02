"""contract.cairo test file."""
import os

import pytest
from starkware.starknet.testing.starknet import Starknet

# The path to the contract source code.
CONTRACT_FILE = os.path.join("contracts", "Poster.cairo")


# The testing library uses python's asyncio. So the following
# decorator and the ``async`` keyword are needed.
@pytest.mark.asyncio
async def test_increase_balance():
  # Create a new Starknet class that simulates the StarkNet
  # system.
  starknet = await Starknet.empty()

  # Deploy the contract.
  contract = await starknet.deploy(source=CONTRACT_FILE)

  # Invoke post().
  await contract.post('ipfs://QmT5htZhqApYpXaWZxJ7mHgzWLALzSSZbNvWanYnvY9BQ2', 'poke').invoke()
