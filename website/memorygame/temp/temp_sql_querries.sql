-- SQLite
select * from memorygame_usermemoryquestionhistory
where user_id=3 and time_stamp>='2019-11-16 17:00';
--and was_correct=0

select * from memorygame_questionlog l 
where l.assigned_to_user_id=3 
and time_stamp>='2019-11-16 17:00';




select * from memorygame_useractiveprogramcontext;


select * from memorygame_assignedprogramuser;


select * from memorygame_question
where time_stamp>='2019-11-16 22:00';
