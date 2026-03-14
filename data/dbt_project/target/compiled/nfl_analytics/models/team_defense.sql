


select
    defteam
    , season
    , median(-epa) as median_def_epa
    , avg(-epa) as mean_def_epa
    , case when mean_def_epa < -0.06 then 'bad'
        when mean_def_epa > 0.06 then 'good'
        else 'average' 
    end as defense_rating
from 
    pbp
where
    play_type in ('pass','run')
group by all