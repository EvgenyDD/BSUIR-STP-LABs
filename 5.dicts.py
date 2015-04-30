a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print('Dict.  a_dict: ' + str(a_dict))
print('a_dict["server"]: ' + str(a_dict['server']))
print('a_dict["database"]: ' + str(a_dict['database']))
print('a_dict["database"] = "blog"')
a_dict['database'] = 'blog'
print('Dict. a_dict: ' + str(a_dict))
print('a_dict["user"] = "mark"')
a_dict['user'] = 'mark'
print('Dict. a_dict: ' + str(a_dict))
print('a_dict["User"] = "mark2"')
a_dict['User'] = 'mark2'
print('Dict. a_dict: ' + str(a_dict))
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
print('Dict. SUFFIXES: ' + str(SUFFIXES))
print('1000 in SUFFIXES: ' + str(1000 in SUFFIXES))
print('SUFFIXES[1000][3]: ' + str(SUFFIXES[1000][3]))
print('++++++++')
print('None - constant.')
