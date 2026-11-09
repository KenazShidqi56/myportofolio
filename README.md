Nama : Kenaz Shidqi Baswara

NPM : 2506558144

Kelas : PBP KKI

[Link] https://kenaz-shidqi-myportofolio.pws.cs.ui.ac.id 

### Assignment 1
1. I don't use those frequently because <div> can already done the job. I often to use <div class="<class name>"> format because it's simple for me.
2. Image position is always facing a problem. I try to use display: flex and some padding command to change its position. I still struggle in parent child class in css.
3. I wanted to make the website has multiple webpages: a project directing to the webpage showing my project.

In this assignment, I didn't use any AI at all. All my sources is from W3School (HTML and CSS), GeekforGeeks (CSS), Stack Overflow (CSS animation and git), and Coding2GO (moving picture animation).

## Assignment 2
1. This is actually a looping operation. First, the user give a response to the webpage, the web will directs the user to another webpage through url. The new webpage will displaying data using template. All data that shown in template is from view, as a separator between the user and the database, that is taken from model. 
2. Imagine the program is used for multi billion dollar company. Hard-coded program only give a single person ownership to the program. By unutilized hard-coded program makes responsibility distribution more possible and easier to manage.
3. For analogy, 'makemigration' is you make the product and 'migrate' is when you publishing it. This is a mandatory part each time any changes on the model.

[AI Usage]
For assignment 2, I didn't use AI at all. The sources I use is from PBP website (workflow from model until the urls), stack overflow (tutorial migration), and youtube (tutorial on making django unit test).

## Assignment 3
1. This step is required to ensure the data is secure.
2. JSON has more advantage than XML: compact size, fast parser, and easy to integrate with javascript.
3. First the client will give a response. The response is send to the "get_json" function. The function will keep the data in JSON.

[AI Usage]
For assignment 3, I use AI tools to help debugging on "add project" button.

## Assignment 6
1. REST is a architecture style for web API. A website is implementing RESTful if it follow several rule: 
    - data treated as a resource.
    - action is depend on HTTP method (GET/PUT/PATCH/DELETE), not by endpoint (projects/editor).
    - It is stateless.
    Put changes entire data in the destination while Patch only change several data.
2. Basically, serializer is divided into two separate purpose:
    - Seralization: change django model into JSON for client.
    - Deseralization: receive JSON input from client into a django model.
    If we use manual dictionary (JsonResponse), user must manually typing code for error code, validation, etc.
3. Authentication identify who is the client and authorization decide what the client can do. If we hide the button without make permission class, client still can execute DELETE through URL endpoint though there is no button for it.
4. The CSRF token avoid any anonymous attack to the website. The program is intentionally bypass client to get through authentication, that's why force_authenticate is not enough.

[AI Usage]
The AI toolkit helps me debugging the api_tests.