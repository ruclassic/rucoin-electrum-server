![electrum-ruc-server](https://raw.githubusercontent.com/ruclassic/rucoin-electrum-server/master/rucoin.png)

electrum-ruc-server for the electrum rucoin client
---------

  * Author: Thomas Voegtlin (Bitcoin Electrum Creator) & Sunerok (RUcoin Fork)
  * Language: Python

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires rucoind v1.1.1 or above, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of RUcoin addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-ruc-server' script



License
-------

Electrum-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
