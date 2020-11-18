"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		Weapon.__name = name
		Weapon.power = power
		Weapon.min_level = min_level

	# classmethod?
	def make_unarmed(self):
		Weapon.__name = Unarmed
		Weapon.power = UNARMED_POWER
		Weapon.min_level = 1


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level):
		Character.name = name
		Character.max_hp = max_hp
		Character.attack = attack
		Character.defense = defense
		Character.level = level

	def compute_damage(self, a, d):
		modifier = crit * random 
		Character.damage = ((2/5 * a.level + 2) * Weapon.power * (a.attack / d.defense) / 50 + 2) * modifier


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
