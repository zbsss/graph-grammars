import unittest

from productions.p1 import P1
from productions.p2 import P2
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph


class TestP2(unittest.TestCase):

    def setUp(self):
        P1(0)

    def test_should_four_fragments(self):
        P2(5)

        draw_graph()

    def test_should_throw_ex_when_root_id_is_missing(self):
        root_id = 5
        vertices_graph_fragment[root_id] = None

        with self.assertRaisesRegex(KeyError, 'Fragment with id 5 does not exist'):
            P2(5)

    def test_should_throw_ex_when_graph_fragment_does_not_contain_five_vertices(self):
        root_id = 5
        vertices_graph_fragment[root_id].vertices.pop(0)
        vertices_graph_fragment[root_id].vertices.pop(0)

        with self.assertRaisesRegex(ValueError, 'Fragment with id 5 contains 3 vertices, but should have 5'):
            P2(5)
