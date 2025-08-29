

with  series_ as (
select
game_id
, season
, series
, series_success
, series_result
, posteam
, defteam
, max(down) as max_down
from
pbp 
where 1=1
-- game_id = '2024_20_BAL_BUF'
	and posteam is not null
	and defteam is not null
	and series_result != 'QB kneel'
	and season >= 2008
	--AND DEFTEAM = 'BUF'
	--and season = 2024
group by all
)
, downs as (
select
	down
	, game_id
	, series
	, play_id
	, ydstogo
	, success
	, penalty
from
pbp 
where
	down = 3
)
, first_3d as (
select game_id
		, series
		, min(play_id) as play_id
from downs 
group by all 
)

, down3 as (
select 
	first_3d.*
	, downs.ydstogo
	, case when downs.ydstogo > 3 then 'long' else 'short' end as distance
	, downs.success
from
	first_3d 
	join downs
		on first_3d.game_id = downs.game_id
			and first_3d.play_id = downs.play_id
)
, sum as (
select *
	, max_down >= 3 as series_3d
	, max_down >= 3 and distance = 'long' as third_and_long
from series_
left join down3
	using(game_id, series)


)

, third_down_conversion as (
	select
game_id
, season
, series
, series_success
, series_result
, posteam
, defteam
, down
, ydstogo
, third_down_converted
, third_down_failed
from
pbp 
where 1=1
-- game_id = '2024_20_BAL_BUF'
	and posteam is not null
	and defteam is not null
	and series_result != 'QB kneel'
	and season >= 2008
	and ((third_down_converted > 0) or (third_down_failed > 0))
group by all
)

, third_down_conversion_sum as (
select
	game_id
	, season
	, posteam
	, sum(third_down_converted) as third_down_converted
	, sum(third_down_failed) as third_down_failed
	, sum(third_down_converted) / (sum(third_down_converted) + sum(third_down_failed)) as third_down_success_rate
	, avg(ydstogo) as avg_ydstogo_3d
from 
	third_down_conversion
group by all
)

select
	sum.game_id
	, sum.posteam
	, sum.defteam
	, count(*) as series_count
	, sum(third_and_long) as third_and_long
	-- how often does a series get to 3rd and long?
	-- less is better
	, sum(cast(third_and_long as real)) / count(*) as third_and_long_rate
	, sum(series_success) / count(*) as series_success_rate
	, third_down_success_rate
	, avg_ydstogo_3d
	
from
	sum
left join
	third_down_conversion_sum using(game_id,posteam)


group by all