import pytest
from cards import Card

@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize(
    "starting_card",
    [
        Card("foo", state="todo"),
        Card("foo", state="in prog"),
        Card("foo", state="done"),
    ],
)
def test_card(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_card[starting_card0]
# test_ids.py::test_card[starting_card1]
# test_ids.py::test_card[starting_card2]

card_list = [
    Card("foo", state="todo"),
    Card("foo", state="in prog"),
    Card("foo", state="done"),
]

@pytest.mark.parametrize("starting_card", card_list, ids=str)
def test_id_str(cards_db, starting_card):
    ...
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_id_str[Card(summary='foo', owner=None, state='todo', id=None)]
# test_ids.py::test_id_str[Card(summary='foo', owner=None, state='in prog', id=None)]
# test_ids.py::test_id_str[Card(summary='foo', owner=None, state='done', id=None)]

def card_state(card):
    return card.state


@pytest.mark.parametrize("starting_card", card_list, ids=card_state)
def test_id_func(cards_db, starting_card):
    ...
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_id_func[todo]
# test_ids.py::test_id_func[in prog]
# test_ids.py::test_id_func[done]

@pytest.mark.parametrize(
    "starting_card", card_list, ids=lambda c: c.state
)
def test_id_lambda(cards_db, starting_card):
    ...
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_id_lambda[todo]
# test_ids.py::test_id_lambda[in prog]
# test_ids.py::test_id_lambda[done]

c_list = [
    Card("foo", state="todo"),
    pytest.param(Card("foo", state="in prog"), id="special"),
    Card("foo", state="done"),
]


@pytest.mark.parametrize("starting_card", c_list, ids=card_state)
def test_id_param(cards_db, starting_card):
    ...
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_id_param[todo] PASSED                                  [ 33%]
# test_ids.py::test_id_param[special] PASSED                               [ 66%]
# test_ids.py::test_id_param[done] PASSED                                  [100%]

id_list = ["todo", "in prog", "done"]


@pytest.mark.parametrize("starting_card", card_list, ids=id_list)
def test_id_list(cards_db, starting_card):
    ...
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"

# test_ids.py::test_id_list[todo]
# test_ids.py::test_id_list[in prog]
# test_ids.py::test_id_list[done]

text_variants = {
    "Short": "x",
    "With Spaces": "x y z",
    "End In Spaces": "x    ",
    "Mixed Case": "SuMmArY wItH MiXeD cAsE",
    "Unicode": "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾",
    "Newlines": "a\nb\nc",
    "Tabs": "a\tb\tc",
}


@pytest.mark.parametrize(
    "variant", text_variants.values(), ids=text_variants.keys()
)
def test_summary_variants(cards_db, variant):
    i = cards_db.add_card(Card(summary=variant))
    c = cards_db.get_card(i)
    assert c.summary == variant

# test_ids.py::test_summary_variants[Short]
# test_ids.py::test_summary_variants[With Spaces]
# test_ids.py::test_summary_variants[End In Spaces]
# test_ids.py::test_summary_variants[Mixed Case]
# test_ids.py::test_summary_variants[Unicode]
# test_ids.py::test_summary_variants[Newlines]
# test_ids.py::test_summary_variants[Tabs]