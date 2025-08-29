
  
    
    

    create  table
      "nfl"."main"."team_offense__dbt_tmp"
  
    as (
      


select
    posteam
    , season
    , median(epa) as median_off_epa
    , avg(epa) as mean_off_epa
    , case when mean_off_epa > 0.06 then 'good'
        when mean_off_epa < 0.06 then 'bad'
        else 'average' 
    end as offense_rating
from 
    pbp
where
    play_type in ('pass','run')
group by all
    );
  
  