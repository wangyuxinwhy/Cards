# -*- coding: utf-8 -*-
from cards import Card


class TestCard:
    def test_card_init(self):
        card = Card(1, "drink water", "wangyuxin", "todo")
        assert card.id == 1
        assert card.summary == "drink water"
        assert card.owner == "wangyuxin"
        assert card.state == "todo"

    # test card from dict
    def test_card_init_from_dict(self):
        card_dict = {"id": 1, "summary": "drink water", "owner": "wangyuxin", "state": "todo"}
        card = Card.from_dict(card_dict)
        card_2 = Card(1, "drink water", "wangyuxin", "todo")
        assert card.id == 1
        assert card.summary == "drink water"
        assert card.owner == "wangyuxin"
        assert card.state == "todo"
        assert card == card_2

    # test card to dict
    def test_card_to_dict(self):
        card_dict = {"id": 1, "summary": "drink water", "owner": "wangyuxin", "state": "todo"}
        card = Card(1, "drink water", "wangyuxin", "todo")
        assert card_dict == card.to_dict()
