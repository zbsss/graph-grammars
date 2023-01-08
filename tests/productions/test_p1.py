import unittest

from productions.p1 import P1
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph


class TestP2(unittest.TestCase):

    def test_should_create_single_fragment(self):
        P1(0)

        draw_graph()

    def test_should_throw_ex_when_fragment_id_not_exist(self):
        root_id = 0
        vertices_graph_fragment[root_id] = None

        with self.assertRaisesRegex(KeyError, 'Fragment with id 0 does not exist'):
            P1(0)
