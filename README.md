# wipedicks
Wipe files and drives securely with randomized ASCII dicks. Because filling hard drives with zeros is really no fun

```
usage: wipedicks.py [-h] [-r] [-n num] [-w] Files [Files ...]

Wipe files/devices with dicks

positional arguments:
  Files                 Files, Directories, and Devices to wipe

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       Recursively parse folders for files to wipe
  -n num, --numrounds num
                        The number of rounds to write the files
  -w, --wipefree        Wipe the free space by creating a large file
```

Example:
```
[root@wipedicks ~]# xxd /dev/sdb | head
0000000: 3823 3d3d 447e 7e7e 2038 3d3d 3d3d 3d3d  8#==D~~~ 8======
0000010: 3d3d 3d3d 447e 7e7e 2038 3d3d 3d3d 3d3d  ====D~~~ 8======
0000020: 3d3d 3d3d 3d3d 447e 7e20 3823 3d3d 3d3d  ======D~~ 8#====
0000030: 3d44 7e20 383d 3d3d 3d3d 3d3d 3d3d 447e  =D~ 8=========D~
0000040: 7e20 3823 3d3d 3d3d 3d3d 3d3d 3d3d 447e  ~ 8#==========D~
0000050: 7e20 3823 3d3d 447e 2038 3d3d 3d3d 3d3d  ~ 8#==D~ 8======
0000060: 3d3d 447e 7e20 3823 3d3d 3d3d 447e 2038  ==D~~ 8#====D~ 8
0000070: 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 4420 383d  ============D 8=
0000080: 3d3d 3d3d 3d3d 3d3d 447e 7e20 3823 3d3d  ========D~~ 8#==
0000090: 3d3d 3d3d 3d3d 3d3d 3d3d 447e 7e20 3823  ==========D~~ 8#
```
