# coding=UTF-8
username = 'User'
password = '1234'
print("{0}'s password is \"{1}\"".format(username, password))


si_suffixes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))
for x in range(8):
    string = "1000{0[" + str(x) +"]} = 1{0[" + str(x) + "]}"
    print(string.format(si_suffixes))

a = 123.45678
print('a = 123.45678')
print('{0:.1f}: ' + '{0:.1f}'.format(a))
print('{0:.2f}: ' + '{0:.2f}'.format(a))
print('{0:.3f}: ' + '{0:.3f}'.format(a))
print('{0:.4f}: ' + '{0:.4f}'.format(a))
print('{0:.5f}: ' + '{0:.5f}'.format(a))
print('{0:.5e}: ' + '{0:.5e}'.format(a))

string = 'AaBbCcDd'
print('string: ' + string)
print('.count("a"): ' + str(string.count('a')))
print('.lower(): ' + string.lower())
print('.lower().count("a"): ' + str(string.lower().count('a')))

string = 'user=pilgrim&database=master&password=1234'
print(string)
print('string.split("&"): ' + str(string.split('&')))
a_list = string.split('&')
print('[v.split("=", 1) for v in ]: \n\t' + str([v.split('=',1) for v in a_list]))
a_list_of_lists = [v.split('=',1) for v in a_list]
print(dict(a_list_of_lists))


a_string = 'My alphabet starts where your alphabet ends.'
print('a_string: ' + a_string)
print('a_string[3:11]: ' + a_string[3:11])
print('a_string[3:-3]: ' + a_string[3:-3])
print('a_string[0:2]: ' + a_string[0:2])
print('a_string[:18]: ' + a_string[:18])
print('a_string[18:]: ' + a_string[18:])

by = b'abcd\x65'
print('Byte string: ' + by)
