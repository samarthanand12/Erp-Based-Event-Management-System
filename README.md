# Erp-Based-Event-Management-System
Highly Reliable and Scalable ERP System

## Abstract:
In today’s world, the trend of websites are changing into Web Applications that acquire logic of problem, interactivity, etc. For developing highly reliable, error free, scalable, fully secure Web Applications Web Developers are using different software engineering techniques. The aim of our application is to deal with the problem of collecting the different ideas from the participants from different parts of the country in a competition and evaluating them for choosing the best one. As there are problem in evaluating the ideas which are collected and ERP divides the submission of the participants between the evaluators so that the evaluation process goes smoothly and error free.

## Introduction:
This paper is all about the solution to the problem which is to collect different ideas from different parts of the country and evaluate them timely and smoothly, there is hard to evaluate creative ideas for a single person in one go.
 So, the application divides those ideas into different users to make the evaluation process easier. Many existing applications can solve this problem but they are not secure, fast, and trustworthy as well. In this web application, we unbiased evaluation process. Besides, it is difficult to find these applications. This application is highly secured and can be accessed via the internet easily. 
The result of our Application comprises of Admin panel and User Panel
Our Web App comprises of two parts – 
1. <a href="mietcsi.tech">Website</a> for collecting submission from the user through various form like Google form and Salesforce web to lead functionality.   
2. <a href="udyat.pythonanywhere.com">ERP System</a> for assigning different ideas to the evaluators and getting response from them in form of evaluation.
## Technology bucket:
1.	Django is a python framework for developing secure web applications. Administration Interface is provided by Django itself. It is scalable and can handle traffic load easily. It has the best security which hides source code and it provides protection against XSS and CSRF attacks, SQL injections, etc. 
2.	Hyper Text Markup Language, Cascade Style Sheets and JavaScript are used to design the front end of the application so that our evaluators and admin can interact with this system effectively and easily. HTML is a markup language supported by all browsers and can integrate with other languages. JavaScript gives the ability to create rich interfaces. It is used everywhere on the web and reduces the demand on the website server.
3.	This also includes some advanced features and automation.


## Body:
This system consists of Admin Panel and User Panel.<br>
<h4>Admin Panel:</h4><br>
<p>Let us discuss about the Admin Panel. Admin Panel has more functionality than User Panel. The overall idea is to take the input from participants through Google form and reflect it to the Admin Panel of the ERP System. Now admin can see the submissions on his screen only after login using his/her Username and Password. Admin has the right to register new evaluators and assign them their respective login IDs and password and assign these submissions to different users (or evaluators). When new users registered by the admin, then the evaluator will get to know their ID and password via mail. Admin has rights to change the password of any user at any time. Besides this, the admin will see the feedback of every evaluation who has the status i.e., whether the submission is accepted or rejected by the evaluator and the reason of acceptance and reason of rejection will also be shown in the system. Only the admin can send mail to the participants whether their submitted idea is accepted or rejected. Two different templates are designed by the developers so that when the admin wants to send mail of acceptance, he selects it by clicking on the button “Send Acceptance Mail” or if the admin wants to send mail of rejection, he has to clicks on the button “Send Rejection Mail” and the mail will be sent to the participant and the participant will be notified immediately. If the admin finds anything wrong with the evaluator or evaluator doesn’t want to evaluate the submitted ideas anymore then the admin has the right to withdraw the evaluation rights from the users (or evaluators). Admin can see all the users under the See Users tab and can check the name as well as the id card of the evaluator (to verify user identity). All these functions which can be done by the admin will be shown on the admin dashboard which will be displayed after admin login.</p>
Flowchart to represent the Admin Panel:

 
<h4>User Panel:</h4><br>
<p>User Panel is also known as Evaluator Panel and it is the most important part of this application. This panel is more restrictive and gives fewer rights are provided to the user. For login on the application, the user has to check his/her mailbox for getting his Username and Password and in that mail, he will also get a link to this application which is accessed via the internet easily. When a User login with their respective Username and Password then he/she see the User Dashboard and on which he sees what he can do i.e., what are the rights given to him. Evaluator can open the submitted idea without knowing from whom it belongs, so that unbiased evaluation can be done. After inspecting the idea user will accept or reject submission according to the appropriateness and the rules on which the ideas should be evaluated and give the reason for accepting it and rejecting it and these both things are reflected in Admin Panel. If the evaluator forgets his/her password he can click on the option “Forgot Password” from the login dashboard and can reset the password and a mail will be sent through which he can reset. In this way, user can evaluate the ideas smoothly.
In this way, ideas submitted by the participants are evaluated smoothly and fast. This process is also represented in the form of figures below: Please refers to the different figures of our application.</p>
Flowchart to represent User Panel:
       


References:
1.	W3schools
2.	Python module 
3.	Salesforce help Articles and DE org
