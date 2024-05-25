# logging adalah menulis pesan mulai dari progress sampai ke masalah kemudian disimpan disebuah file untuk meminimalisasi sebuah bug
# ada 5 level logging : 1. debug 2. info 3. warning 4. error 5. critical
import logging
# dir_log = dir(logging)
# print(dir_log)

# membuat dan mengkonfigurasi logger
# path file berada
# untuk mengganti sebuah logging format membuat string dengan desired attribute
log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename= "E:\\Lumberjack.log", level= logging.DEBUG , format= log_format, filemode= 'w')# -> maka untuk memperbaikinya
logger = logging.getLogger()

# tes sebuah logg
# menampilkan info logg
logger.info('yyyy')

print(logger.level)

# 30 apa artinya ?
# didalam sebuah logging module, ada 6 built in level konstan, seperti :
# not set, debug, info, warning, eror, critical
# lvl notset = 0, lvl debug = 10, lvl info = 20, lvl warning = 30, lvl eror = 40
# maka berarti 30 diatas menunjukkan pada level warning ->

# tes pesan
# mari buat pesan dari kelima level bersamaan
logger.debug('debug coyy')
logger.info('info coyy')
logger.warning('peringatan coyy')
logger.error('eror coyy')
logger.critical('critcal coyy')

