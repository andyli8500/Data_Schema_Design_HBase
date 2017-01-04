# Data_Schema_Design_HBase
Design data schema for movie rating data to support queries in HBase


## This whole program is recommended to excute under thrift server.


### Import Schema Using following command
------------------------------------
    $ hbase shell index_table.txt

Or if interested in the base table, run following as well:
    $ hbase shell Schema_base.txt
====================================

### Running Queries With Python Program
===================================
1. Runing First Query:
    $ python2 hb.py q1 <userID>

2. Second Query:
    $ python2 hb.py q2 <artistName>

3. Third Query:
    $ python2 hb.py q3 <artistName>

4. Forth Query:
    $ python2 hb.py q4 <userID>