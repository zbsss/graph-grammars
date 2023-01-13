import unittest

from productions.p1 import P1
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph
from utils.vertex import VertexLabel


class TestP2(unittest.TestCase):

    def test_should_create_single_fragment(self):
        P1(0)

        draw_graph()

    def test_should_throw_ex_when_fragment_id_not_exist(self):
        root_id = 0
        vertices_graph_fragment[root_id] = None

        with self.assertRaisesRegex(Exception, 'Fragment with id 0 does not exist'):
            P1(0)

    def test_should_throw_ex_when_root_type_is_incorrect(self):
        root_id = 0
        vertices_graph_fragment[root_id].middle_vertex.label = VertexLabel.E

        with self.assertRaisesRegex(Exception, 'Incorrect type of middle vertex for fragment with id 0.'
                                               ' Expected type is I, but we actual type is E'):
            P1(0)
