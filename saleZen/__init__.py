import pymysql
pymysql.version_info = (2, 2, 8, "final", 0) # এখানে ভার্সনটি লিখে দিলে ডিয়াঙ্গো আর ঝামেলা করবে না
pymysql.install_as_MySQLdb()