Serie of data of 20 items
Create direction for accessing server:Data, Routes(2), app key
readme
software:consume API, readme

The web contains data about possible fail rate for students in Gamedesign 3, using a~z as representation.

The list includes: a,b,c,d,e,f,g,h,i,l,m,o,p,q,r,y,x,z.

   

Using: /class_pass_chance/{participant_name}/fail_chance , will lead to the chance to fail and the student's name (a~z)
Using: /class_pass_chance/{participant_name}/age , will lead to the age and participant name
Using: "/class_pass_chance/info" will lead to introduction.
Using: "/class_pass_chance/get_key" to get api key
if the key is incorrect, remember to insert the correct key
Note that, API_KEYS = ["060501", "060212"]

I named it api_key, so remember to add the api_key at the end of the route, like the sample lower.

Again, always remember add "?api_key=" and the correct key

sample: http://10.6.20.246:8000/class_pass_chance/a/age?api_key=060212
