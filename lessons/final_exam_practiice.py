"""Final Exam Practice Problems."""

def free_biscuits(game_data: dict[str, list[int]]) -> dict[str, bool]:
    """Returns if free biscuits were earned."""
    new_dict: dict[str, bool] = {}
    
    for game, points in game_data:
        total_points: int = 0
        for player in points:
            total_points += player
            if total_points >= 100:
                new_dict[game] = True
            else:
                new_dict[game] = False
    return new_dict


    