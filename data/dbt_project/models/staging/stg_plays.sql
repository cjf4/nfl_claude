-- Staging model for play-by-play data
-- Cleans and standardizes the raw nflfastr data

{{ config(materialized='view') }}

select
    play_id,
    game_id,
    season,
    week,
    game_date,
    home_team,
    away_team,
    posteam as possession_team,
    defteam as defense_team,
    play_type,
    down,
    ydstogo as yards_to_go,
    yardline_100,
    qtr as quarter,
    time,
    yards_gained,
    touchdown,
    fumble,
    interception,
    safety,
    penalty,
    first_down,
    epa,
    wp as win_probability,
    wpa as win_probability_added
from {{ ref('pbp_all') }}
where play_type is not null