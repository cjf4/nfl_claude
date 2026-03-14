

select
    game_id
    , posteam
    , defteam
    , season
    , week
    , season_type
    , avg(epa) as avg_off_epa
    , avg(-epa) as avg_def_epa
from
    pbp
where 
    posteam is not null
    and defteam is not null
group by all