"""Hash Table implementation"""

import typing
import logging

logging.getLogger().setLevel(logging.DEBUG)


def main():
  table = HashTable(11)
  logging.info(table.slot_key)

  table.Put(50, 'muh-data')
  logging.info(table.slot_key)

  table.Put(22, 'moar data')
  logging.info(table.slot_key)

  table.Put(34, 'shwiffty')
  logging.info(table.slot_key)


  table.Put(33, 'rick')
  logging.info(table.slot_key)

  table.Put(33, 'morty')
  logging.info(table.slot_key)


class HashTable:
  def __init__(self, size):
    self.size = size
    self.slot_key = [None] * self.size
    self.slot_data = [None] * self.size


  def Put(self, key, data):
    remainder_key_hash = self.remainderHash(key)
    logging.info(f'HASH: {key} -> {remainder_key_hash}')

    if self.slot_key[remainder_key_hash] == None:
      logging.debug(f'Found slot for key: {key}')
      self.slot_key[remainder_key_hash] = key
      self.slot_data[remainder_key_hash] = data
    elif self.slot_key[remainder_key_hash] == key:
      logging.debug(f'Found same key: {key} - overriding')

      self.slot_data[remainder_key_hash] = data
    else:
      logging.debug(f'Collision: Rehashing key {key}')
      self.Put(self.rehash(remainder_key_hash), data)


    print('\n')

  def remainderHash(self, key) -> int:
    return key % self.size


  def rehash(self, key) -> int:
    """Since key position is taken, move input by one
    then hash again.
    """
    return (key + 1) % self.size



if __name__ == '__main__':
  main()
