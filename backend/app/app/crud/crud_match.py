import logging

from sqlalchemy.orm import Session
from app.models import Match, MatchEventOdds
from app.schemas import MatchResponse
from fastapi import Depends, FastAPI

logging.basicConfig(level=logging.DEBUG)

def get_matches(db: Session, skip: int, limit: int):
    return db.query(Match).offset(skip).limit(limit).all()


def get_match(db: Session, id: int):
    return db.query(Match).get(id)


def create_match(db: Session, *, obj_in: MatchResponse) -> Match:
    match = Match(
        first_fighter_id=obj_in.first_fighter_id,
        second_fighter_id=obj_in.second_fighter_id,
    )
    
    db.add(match)
    db.commit()
    db.refresh(match)

    match_odds_win_1 = MatchEventOdds(match_id=match.id, match_event_id=1, odds=1.0)
    match_odds_win_2 = MatchEventOdds(match_id=match.id, match_event_id=2, odds=1.0)

    db.add(match_odds_win_1)
    db.add(match_odds_win_2)
    db.commit()
    db.refresh(match_odds_win_1)
    db.refresh(match_odds_win_2)
    logging.info('Created match & match_odds')

    match.match_odds.append(match_odds_win_1)
    match.match_odds.append(match_odds_win_2)

    db.commit()
    db.refresh(match)

    logging.info(match)
    logging.info(match.match_odds)

    return match
