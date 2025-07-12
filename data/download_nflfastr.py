#!/usr/bin/env python3
"""
Simple script to create sample NFL data for testing the pipeline.
Will download actual data once we confirm the correct URLs.
"""

import duckdb
import pandas as pd
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Paths
DATA_DIR = Path(__file__).parent
DB_PATH = DATA_DIR / "nfl.duckdb"

def create_sample_data(season):
    """Create comprehensive sample NFL data with major nflfastR columns for a given season."""
    logger.info(f"Creating comprehensive sample NFL data for {season}...")
    
    import random
    import numpy as np
    
    n_plays = 100
    
    # Core nflfastR columns based on research
    sample_data = {
        # Game/Play Identifiers
        'play_id': range(1, n_plays + 1),
        'game_id': [f'{season}_01_BUF_MIA'] * 50 + [f'{season}_01_KC_DEN'] * 50,
        'old_game_id': [f'{season}091000'] * 50 + [f'{season}091100'] * 50,
        'season': [season] * n_plays,
        'season_type': ['REG'] * n_plays,
        'week': [1] * n_plays,
        'game_date': [f'{season}-09-10'] * 50 + [f'{season}-09-11'] * 50,
        
        # Team Information
        'home_team': ['MIA'] * 50 + ['DEN'] * 50,
        'away_team': ['BUF'] * 50 + ['KC'] * 50,
        'posteam': (['BUF', 'MIA'] * 25) + (['KC', 'DEN'] * 25),
        'posteam_type': (['away', 'home'] * 25) + (['away', 'home'] * 25),
        'defteam': (['MIA', 'BUF'] * 25) + (['DEN', 'KC'] * 25),
        
        # Game State
        'qtr': ([1, 1, 2, 2] * 25),
        'quarter_seconds_remaining': [random.randint(0, 900) for _ in range(n_plays)],
        'half_seconds_remaining': [random.randint(0, 1800) for _ in range(n_plays)],
        'game_seconds_remaining': [random.randint(0, 3600) for _ in range(n_plays)],
        'game_half': (['Half1', 'Half1', 'Half2', 'Half2'] * 25),
        'quarter_end': [0] * 98 + [1, 1],
        'drive': [random.randint(1, 15) for _ in range(n_plays)],
        'sp': [random.choice([0, 1]) for _ in range(n_plays)],
        
        # Play Details
        'down': ([1, 2, 3, 4] * 25),
        'goal_to_go': [random.choice([0, 1]) for _ in range(n_plays)],
        'time': [f"{random.randint(0,15):02d}:{random.randint(0,59):02d}" for _ in range(n_plays)],
        'yrdln': [f"BUF {random.randint(1,50)}" for _ in range(n_plays)],
        'ydstogo': ([10, 8, 5, 3] * 25),
        'ydsnet': [random.randint(-20, 80) for _ in range(n_plays)],
        'desc': [f"Sample play description {i}" for i in range(1, n_plays + 1)],
        'play_type': (['pass', 'run', 'punt', 'field_goal'] * 25),
        'yards_gained': ([5, 3, 0, 45] * 25),
        'shotgun': [random.choice([0, 1]) for _ in range(n_plays)],
        'no_huddle': [random.choice([0, 1]) for _ in range(n_plays)],
        'qb_dropback': [random.choice([0, 1]) for _ in range(n_plays)],
        'qb_kneel': [0] * 98 + [1, 1],
        'qb_spike': [0] * 95 + [1] * 5,
        'qb_scramble': [random.choice([0, 1]) for _ in range(n_plays)],
        
        # Passing
        'pass_length': [random.choice(['short', 'deep', None]) for _ in range(n_plays)],
        'pass_location': [random.choice(['left', 'middle', 'right', None]) for _ in range(n_plays)],
        'air_yards': [random.randint(-5, 40) if random.random() > 0.3 else None for _ in range(n_plays)],
        'yards_after_catch': [random.randint(0, 20) if random.random() > 0.3 else None for _ in range(n_plays)],
        
        # Rushing
        'run_location': [random.choice(['left', 'middle', 'right', None]) for _ in range(n_plays)],
        'run_gap': [random.choice(['guard', 'tackle', 'end', None]) for _ in range(n_plays)],
        
        # Kicking
        'field_goal_result': [random.choice(['good', 'missed', 'blocked', None]) for _ in range(n_plays)],
        'kick_distance': [random.randint(18, 65) if random.random() > 0.8 else None for _ in range(n_plays)],
        'extra_point_result': [random.choice(['good', 'failed', 'blocked', None]) for _ in range(n_plays)],
        'two_point_conv_result': [random.choice(['success', 'failure', None]) for _ in range(n_plays)],
        
        # Timeouts
        'home_timeouts_remaining': [random.randint(0, 3) for _ in range(n_plays)],
        'away_timeouts_remaining': [random.randint(0, 3) for _ in range(n_plays)],
        'posteam_timeouts_remaining': [random.randint(0, 3) for _ in range(n_plays)],
        'defteam_timeouts_remaining': [random.randint(0, 3) for _ in range(n_plays)],
        'timeout': [random.choice([0, 1]) for _ in range(n_plays)],
        'timeout_team': [random.choice(['home', 'away', None]) for _ in range(n_plays)],
        
        # Scoring
        'touchdown': ([0, 0, 0, 1] * 25),
        'pass_touchdown': [random.choice([0, 1]) if random.random() > 0.9 else 0 for _ in range(n_plays)],
        'rush_touchdown': [random.choice([0, 1]) if random.random() > 0.9 else 0 for _ in range(n_plays)],
        'return_touchdown': [0] * n_plays,
        'fumble': ([0] * n_plays),
        'fumble_forced': [0] * n_plays,
        'fumble_not_forced': [0] * n_plays,
        'fumble_out_of_bounds': [0] * n_plays,
        'solo_tackle': [random.choice([0, 1]) for _ in range(n_plays)],
        'safety': ([0] * n_plays),
        'penalty': ([0] * 90 + [1] * 10),
        'tackled_for_loss': [random.choice([0, 1]) for _ in range(n_plays)],
        'fumble_lost': [0] * n_plays,
        'own_kickoff': [0] * n_plays,
        'own_kickoff_recovery': [0] * n_plays,
        'own_kickoff_recovery_td': [0] * n_plays,
        
        # Interceptions
        'interception': ([0] * 95 + [1] * 5),
        'lateral_interception': [0] * n_plays,
        
        # Penalties
        'penalty_team': [random.choice(['BUF', 'MIA', 'KC', 'DEN', None]) for _ in range(n_plays)],
        'penalty_player_id': [None] * n_plays,
        'penalty_player_name': [None] * n_plays,
        'penalty_yards': [random.randint(5, 15) if random.random() > 0.9 else None for _ in range(n_plays)],
        
        # First Downs
        'first_down': ([1, 0, 0, 1] * 25),
        'first_down_pass': [random.choice([0, 1]) for _ in range(n_plays)],
        'first_down_rush': [random.choice([0, 1]) for _ in range(n_plays)],
        'first_down_penalty': [random.choice([0, 1]) for _ in range(n_plays)],
        
        # Player Information (simplified)
        'passer_player_id': [f"00-000{random.randint(1000,9999)}" if random.random() > 0.3 else None for _ in range(n_plays)],
        'passer_player_name': [f"QB {random.randint(1,30)}" if random.random() > 0.3 else None for _ in range(n_plays)],
        'passing_yards': [random.randint(-10, 50) if random.random() > 0.3 else None for _ in range(n_plays)],
        'receiver_player_id': [f"00-000{random.randint(1000,9999)}" if random.random() > 0.5 else None for _ in range(n_plays)],
        'receiver_player_name': [f"WR {random.randint(1,30)}" if random.random() > 0.5 else None for _ in range(n_plays)],
        'receiving_yards': [random.randint(0, 80) if random.random() > 0.5 else None for _ in range(n_plays)],
        'rusher_player_id': [f"00-000{random.randint(1000,9999)}" if random.random() > 0.4 else None for _ in range(n_plays)],
        'rusher_player_name': [f"RB {random.randint(1,30)}" if random.random() > 0.4 else None for _ in range(n_plays)],
        'rushing_yards': [random.randint(-5, 30) if random.random() > 0.4 else None for _ in range(n_plays)],
        
        # Advanced Metrics
        'epa': [round(random.uniform(-3.0, 3.0), 3) for _ in range(n_plays)],
        'ep': [round(random.uniform(-2.0, 7.0), 3) for _ in range(n_plays)],
        'air_epa': [round(random.uniform(-2.0, 2.0), 3) if random.random() > 0.3 else None for _ in range(n_plays)],
        'yac_epa': [round(random.uniform(-1.0, 2.0), 3) if random.random() > 0.3 else None for _ in range(n_plays)],
        'comp_air_epa': [round(random.uniform(-1.0, 3.0), 3) if random.random() > 0.5 else None for _ in range(n_plays)],
        'comp_yac_epa': [round(random.uniform(-1.0, 2.0), 3) if random.random() > 0.5 else None for _ in range(n_plays)],
        
        # Win Probability
        'wp': [round(random.uniform(0.1, 0.9), 3) for _ in range(n_plays)],
        'wpa': [round(random.uniform(-0.2, 0.2), 4) for _ in range(n_plays)],
        'home_wp': [round(random.uniform(0.1, 0.9), 3) for _ in range(n_plays)],
        'away_wp': [round(random.uniform(0.1, 0.9), 3) for _ in range(n_plays)],
        
        # Scores
        'total_home_score': [random.randint(0, 35) for _ in range(n_plays)],
        'total_away_score': [random.randint(0, 35) for _ in range(n_plays)],
        'posteam_score': [random.randint(0, 35) for _ in range(n_plays)],
        'defteam_score': [random.randint(0, 35) for _ in range(n_plays)],
        'score_differential': [random.randint(-21, 21) for _ in range(n_plays)],
        'posteam_score_post': [random.randint(0, 35) for _ in range(n_plays)],
        'defteam_score_post': [random.randint(0, 35) for _ in range(n_plays)],
        'score_differential_post': [random.randint(-21, 21) for _ in range(n_plays)],
        
        # Field Position
        'yardline_100': range(100, 0, -1),
        'side_of_field': [random.choice(['BUF', 'MIA', 'KC', 'DEN']) for _ in range(n_plays)],
        
        # Additional Common Columns
        'complete_pass': [random.choice([0, 1]) if random.random() > 0.3 else None for _ in range(n_plays)],
        'incomplete_pass': [random.choice([0, 1]) if random.random() > 0.3 else None for _ in range(n_plays)],
        'pass_attempt': [random.choice([0, 1]) for _ in range(n_plays)],
        'rush_attempt': [random.choice([0, 1]) for _ in range(n_plays)],
        'special_teams_play': [random.choice([0, 1]) for _ in range(n_plays)],
        'st_play_type': [random.choice(['punt', 'kickoff', 'field_goal', None]) for _ in range(n_plays)],
    }
    
    logger.info(f"Created sample data with {len(sample_data)} columns")
    return pd.DataFrame(sample_data)

def update_database():
    """Create sample database for testing with multiple seasons."""
    conn = duckdb.connect(str(DB_PATH))
    
    # Create sample data for 2020-2024
    seasons = [2020, 2021, 2022, 2023, 2024]
    union_clauses = []
    
    for season in seasons:
        df = create_sample_data(season)
        
        # Store in DuckDB
        conn.execute(f"DROP TABLE IF EXISTS pbp_{season}")
        conn.execute(f"CREATE TABLE pbp_{season} AS SELECT * FROM df")
        logger.info(f"Created sample table with {len(df)} plays for {season}")
        
        union_clauses.append(f"SELECT * FROM pbp_{season}")
    
    # Create unified view with all seasons
    union_query = " UNION ALL ".join(union_clauses)
    conn.execute(f"""
        CREATE OR REPLACE VIEW pbp_all AS
        {union_query}
    """)
    
    # Show summary
    result = conn.execute("SELECT COUNT(*) as total_plays FROM pbp_all").fetchone()
    logger.info(f"Total plays in database: {result[0]:,}")
    
    # Show seasons
    seasons_result = conn.execute("""
        SELECT season, COUNT(*) as plays 
        FROM pbp_all 
        GROUP BY season 
        ORDER BY season
    """).fetchall()
    
    logger.info("Seasons in database:")
    for season, plays in seasons_result:
        logger.info(f"  {season}: {plays:,} plays")
    
    # Show teams
    teams_result = conn.execute("""
        SELECT posteam as team, COUNT(*) as plays 
        FROM pbp_all 
        WHERE posteam IS NOT NULL 
        GROUP BY posteam 
        ORDER BY plays DESC
    """).fetchall()
    
    logger.info("Teams in database:")
    for team, plays in teams_result:
        logger.info(f"  {team}: {plays:,} plays")
    
    conn.close()
    logger.info(f"Sample database created at {DB_PATH}")
    logger.info("\nNext steps:")
    logger.info("1. Update this script with correct nflfastr URLs")
    logger.info("2. Test the analysis notebook")
    logger.info("3. Set up dbt transformations")

if __name__ == "__main__":
    update_database()