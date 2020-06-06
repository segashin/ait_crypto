CBC-MAC forgery
===============

You have two binary files in the handout folder, file1.bin and file2.bin, and their CBC-MAC values in file1-mac.bin and file2-mac.bin, respectively.  Try to merge file1.bin and file2.bin (in this order) to obtain file12.bin such that file2-mac.bin verifies correctly on file12.bin. Then, try to merge file2.bin and file1.bin (in this order) to obtain file21.bin such that file1-mac.bin verifies correctly on file21.bin. You need to do a bit more than just simple concatenation of the files...

In order to verify if your forgery works, use the attached CBC-MAC verification script (cbcmac-ver.py) with the key string "0123456789abcdef".
