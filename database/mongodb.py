from pymongo import MongoClient
import os


class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/snake_scores')
        self.db = self.client['snake_scores']
        self.collection = self.db['scores']

    def save_score(self, name, score, grid_size):
        player = self.collection.find_one({"name": name})
        if player:
            if score > player["score"]:
                self.collection.update_one({"name": name},
                                           {"$set": {"score": score, "grid_size": grid_size}})
        else:
            score_data = {"name": name, "score": score, "grid_size": grid_size}
            self.collection.insert_one(score_data)

    def get_highest_score(self, name):
        player = self.collection.find_one({"name": name})
        if player:
            return player["score"]
        return 0

    def get_grid_size(self, name):
        player = self.collection.find_one({"name": name})
        if player:
            return player["grid_size"]
        return 0
