"""
Overview
We're building an online platform that connects people with fitness coaches 
for live workout sessions over Zoom. The platform works through coordinators 
who manage everything about the sessions - from scheduling to coach assignments. 
Users can buy different plans to join these sessions, ranging from a basic package 
with limited sessions to unlimited access. Think of it as a virtual gym where you can 
join any class that fits your schedule, guided by professional coaches from your home. 
The whole system is designed to be easy to use: coordinators set up sessions, users book 
them based on their plans, and everyone gets helpful reminders to make sure they don't miss their workouts.

Session Management

Coordinators create and manage all workout sessions on our platform. They decide 
everything about a session - what type of workout it is (like yoga or HIIT), how long 
it runs (30, 45, or 60 minutes), and how many people can join that specific session. 
They also pick which coach will teach it and set up the Zoom link. When users want to
 join a class, they can easily search for sessions based on what time they want to work out
 , what type of exercise they want to do, which coach they prefer, or how challenging they want
   the workout to be(Level - Beginner/Intermediate/Expert). Once enough people have signed up for 
   a session (based on the limit set by the coordinator), no one else can book that session. 
Existing Models




user----coordinator---coach


User
	user_id (int)  (Primary key)
	Username (str)
	Type (user/coach/coordinator) (Enum)




WorkOutType:
    Yoga
    Gym

    # coordinator

Workout:
    type--enum---WorkOutType
    datetime
    max_people
    session_duration
    is_active: default--True
    coach_id--not null

coach_id, 9-10, 10-11,..............
            True
#coach
CoachSessionInfo:
    user_id
    workout_session_id
    is_done

    
add new workout sessions 
Post-->version/api/workouts
    {
        "type": "",
        "datetime": "",
        "max_people":"",
        "session_duration":"",
        "coach_id": ""-->
    }

get workout sessions data
Get-->version/api/workouts
    params--for filter--we can add here

    
modify existing workout sessions 
Patch-->version/api/workouts/id
    {
    "is_active": False
    }
    ----> booked--> TODO:

    
delete existing workout sessions 
Delete-->version/api/workouts/id
    


    

    
Plan
	plan_id (int) (Primary key)
	Name (str)
	Duration_in_days(int)--validity
	Session_count (int)--


     
UserSubscription:
    id
    user_id
    plan_id
    remaining_session
    # ---discuss further for plan--expiry


    
UserBookedActivity:
    id
    UserSubscription_id
    workout_id
    status--boolean--enum---created---attended--cancelled
    



view plans
Get-->version/api/plans


book plan
Post-->version/api/book_plan
{
    "Name"
	"Duration_in_days"
	"Session_count"
    user_id
}------------------------> UserSubscription


view activity
Get-->version/api/ativities
-->id or token we can collect on header


add activity
Post-->version/api/ativities
{
    "id"
    "UserSubscription_id"
    "workout_id"
}


mark activity done or cancel
Patch-->version/api/ativities
{
    "status"
}















    

"""