## Info o słownikach:

```
slownik = {"imie": "Adam"}
slownik["imie"]
'Adam'
slownik["nazwisko"]
Traceback(most
recent
call
last):
File
"/usr/lib/python3.10/idlelib/run.py", line
578, in runcode
exec(code, self.locals)
File
"<pyshell#2>", line
1, in < module >
KeyError: 'nazwisko'
slownik["nazwisko"] = "Jurkiewicz"
slownik.keys()
dict_keys(['imie', 'nazwisko'])
slownik.values()
dict_values(['Adam', 'Jurkiewicz'])
for keyname in slownik:
    print(f"{keyname=}, {slownik[keyname]=}")

keyname = 'imie', slownik[keyname] = 'Adam'
keyname = 'nazwisko', slownik[keyname] = 'Jurkiewicz'
```