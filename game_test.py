from game import Game

from unittest import mock
import unittest

class TestGame(unittest.TestCase):
    
    def test_initialize_field(self):
        game_instance = Game()
        field = game_instance.initialize_field()

        expected_list = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(field, expected_list)

    def test_instantiate_players(self):
        game_instance = Game()
        expected_player1 = "X"
        expected_player2 = "O"
        
        player1, player2 = game_instance.instatiate_players()

        self.assertEqual(player1, expected_player1)
        self.assertEqual(player2, expected_player2)
    
    def test_player1_play(self):
        game_instance = Game()

        #Start empty field
        game_instance.start_game()

        column = 1
        row = 1
        game_instance.player1_play(row, column)

        expected_field = [
            [' ', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', ' ']
        ]

        self.assertEqual(game_instance.field, expected_field)

        expected_field = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', 'X', ' ']
        ]
        self.field = game_instance.initialize_field()
        column = 1
        row = 2
        game_instance.player1_play(row, column)

        self.assertEqual(self.field, expected_field)

        expected_field = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['X', ' ', ' ']
        ]
        self.field = game_instance.initialize_field()
        column = 0
        row = 2
        game_instance.player1_play(row, column)

        self.assertEqual(self.field, expected_field)
    
    def test_player2_play(self):
        game_instance = Game()

        #Initialize empty field
        game_instance.start_game()
        player1_column = 0
        player1_row = 2
        game_instance.player1_play(player1_row, player1_column)

        player2_column = 1
        player2_row = 1

        game_instance.player2_play(player2_row, player2_column)

        expected_field = [
            [' ', ' ', ' '],
            [' ', 'O', ' '],
            ['X', ' ', ' ']
        ]

        self.assertEqual(game_instance.field, expected_field)
    
    def test_check_empty_field(self):
        game_instance = Game()

        #Initialize empty field
        self.field = game_instance.start_game()

        #Populate field
        game_instance.player1_play(2,0)
        game_instance.player2_play(1,1)
        
        expected_not_empty = game_instance.check_empty_field(1,1)
        
        self.assertFalse(expected_not_empty)

        expected_empty = game_instance.check_empty_field(0,0)
        self.assertTrue(expected_empty)

    def test_check_winning_conditions(self):
        game_instace = Game()
        expected_field_column = [
            ['X', ' ', ' '],
            ['X', ' ', ' '],
            ['X', ' ', ' ']
        ]
        game_instace.field =  expected_field_column
        winning_condition = game_instace.check_winning_conditions()
        self.assertTrue(winning_condition)

        expected_field_row = [
            ['O', 'O', 'O'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game_instace.field =  expected_field_row
        winning_condition = game_instace.check_winning_conditions()
        self.assertTrue(winning_condition)

        expected_field_diagonals = [
            ['O', 'O', 'O'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game_instace.field =  expected_field_diagonals
        winning_condition = game_instace.check_winning_conditions()
        self.assertTrue(winning_condition)

        expected_field_win_diagonal = [
            ['O', ' ', 'O'],
            [' ', 'O', ' '],
            [' ', ' ', 'O']
        ]
        game_instace.field =  expected_field_win_diagonal
        winning_condition = game_instace.check_winning_conditions()
        self.assertTrue(winning_condition)

        expected_field_win_diagonal = [
            ['O', ' ', 'X'],
            [' ', 'X', ' '],
            ['X', ' ', 'O']
        ]
        game_instace.field =  expected_field_win_diagonal
        winning_condition = game_instace.check_winning_conditions()
        self.assertTrue(winning_condition)

        expected_field_not_win = [
            ['O', ' ', 'X'],
            [' ', ' ', ' '],
            ['X', ' ', 'O']
        ]
        game_instace.field =  expected_field_not_win
        not_winning_condition = game_instace.check_winning_conditions()
        self.assertFalse(not_winning_condition)


    def test_start_game(self):
        game_instance = Game()
        game_instance.start_game()        
        self.assertEqual(game_instance.field, game_instance.initialize_field())       

    def test_player1_turn_empty_field(self):
        with mock.patch('builtins.input', side_effect=['2', '2']):
            game_instance = Game()

            game_instance.initialize_field()
            game_instance.instatiate_players()
            game_instance.player1_turn()

    def test_player1_turn_filled_field(self):
        with mock.patch('builtins.input', side_effect=['2', '2','1','0']):
            game_instance = Game()

            game_instance.initialize_field()
            
            game_instance.field = [
            [' ', ' ', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X']]

            game_instance.instatiate_players()
            game_instance.player1_turn()

    def test_play_game_player1_wins(self):
        with mock.patch('builtins.input', side_effect=[
                                        '0', '0',
                                        '1', '2',
                                        '1', '1',
                                        '0', '1',
                                        '2', '2'

                                        ]):
            game_instance = Game()

            game_instance.play_game()

        self.assertEqual(game_instance.player1, game_instance.winning_player)

        

    def test_play_game_player2_wins(self):
        game_instance = Game()

        
        game_instance.instatiate_players()
        game_instance.start_game()

        player2 = game_instance.player2

        game_instance.player1_play(1,2)
        game_instance.player2_play(0,0)

        game_instance.player1_play(0,1)
        game_instance.player2_play(1,1)

        game_instance.player1_play(0,2)
        game_instance.player2_play(2,2)
        with mock.patch('builtins.input', side_effect=[
                                        '1', '2',
                                        '0', '0',
                                        '0', '1',
                                        '1', '1',
                                        '0',  '2',
                                        '2',  '2'
                                        ]):
            game_instance = Game()

            game_instance.play_game()

        self.assertEqual(game_instance.player2, game_instance.winning_player)

        