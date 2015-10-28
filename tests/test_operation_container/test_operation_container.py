"""Test the creation of OperationContainer objects."""

from __future__ import absolute_import
import unittest
import copy

import trade
from .container_test_base import TestFetchPositions
from tests.fixtures.operations import (
    OPERATION24, OPERATION45
)
from tests.fixtures.commissions import (
    COMMISSIONS12
)
from tests.fixtures.assets import (
    ASSET,
)


class TestContainerCreationCase00(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        self.container = trade.OperationContainer()

    def test_container_exists(self):
        self.assertTrue(self.container)


class TestContainerCreationCase01(unittest.TestCase):
    """Test the creation of a OperationContainer."""

    def setUp(self):
        self.container = trade.OperationContainer()
        self.container.commissions = COMMISSIONS12
        self.container.fetch_positions_tasks = [
            trade.plugins.fetch_exercises,
            trade.plugins.fetch_daytrades,
        ]
        self.container.fetch_positions()

    def test_container_exists(self):
        self.assertTrue(self.container)

    def test_container_commissions(self):
        self.assertEqual(self.container.commissions, COMMISSIONS12)


class TestContainerAddToPositions(TestFetchPositions):
    """Test add_to_position_operations method."""

    operations = [OPERATION24]
    positions = {
        ASSET.symbol: {
            'quantity': 20,
            'price': 3,
            'volume': 60,
        },
    }

    def setUp(self):
        super(TestContainerAddToPositions, self).setUp()
        self.container.add_to_position_operations(copy.deepcopy(OPERATION45))

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)
