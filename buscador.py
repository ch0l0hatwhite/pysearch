import webbrowser as cholo
import time

print("""

:::::::::  :::   :::                                               
:+:    :+: :+:   :+:                                               
+:+    +:+  +:+ +:+                                                
+#++:++#+    +#++:                                                 
+#+           +#+                                                  
#+#           #+#                                                  
###           ###                                                  
 ::::::::  ::::::::::     :::     :::::::::   ::::::::  :::    ::: 
:+:    :+: :+:          :+: :+:   :+:    :+: :+:    :+: :+:    :+: 
+:+        +:+         +:+   +:+  +:+    +:+ +:+        +:+    +:+ 
+#++:++#++ +#++:++#   +#++:++#++: +#++:++#:  +#+        +#++:++#++ 
       +#+ +#+        +#+     +#+ +#+    +#+ +#+        +#+    +#+ 
#+#    #+# #+#        #+#     #+# #+#    #+# #+#    #+# #+#    #+# 
 ########  ########## ###     ### ###    ###  ########  ###    ### 
                                                               
                                                               

""")
a=input("Ingrese su busqueda > ")
print("\n")
for i in range(4):
	time.sleep(0.5)
	print(" su busqueda esta en camino...\n")
    
b=(" &oq=nutr&aqs=chrome.1.69i57j0i67i433l2j0i131i433j0i67.1611j0j9&client=ms-android-americamovil-mx-revc&sourceid=chrome-mobile&ie=UTF-8")
f=("https://www.google.com/search?q="+a + b)

print("su busqueda de : "+a,"esta lista!")
time.sleep(2)
cholo.open(f)

