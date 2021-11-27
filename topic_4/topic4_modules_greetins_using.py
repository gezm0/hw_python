# import only one function

#from topic4_modules_greetings import polite
#polite('Valentin')

# import all functions

#import topic4_modules_greetings

#topic4_modules_greetings.polite('Valentin')
#topic4_modules_greetings.not_so_polite('Misha')

# this allow rename external functions for internal use

#from topic4_modules_greetings import polite as formal
#from topic4_modules_greetings import not_so_polite as informal

#formal('Valentin')
#informal('Misha')

# 'import as' allow rename external functions for internal use

import topic4_modules_greetings as hello

hello.polite('Valentin')
hello.not_so_polite('Misha')

# that's how to see all functions in module
print(dir(hello))

print("Name of module file:", hello.__name__)
print("Name of module file full name:", hello.__file__)
