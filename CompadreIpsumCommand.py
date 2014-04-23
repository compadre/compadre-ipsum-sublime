# -*- coding: utf-8 -*-

import sublime, sublime_plugin, re

class CompadreIpsum():
	__para = [
		u"Eiiitaaa Mainhaaa!! Esse Lorem ipsum é só na sacanageeem!! E que abundância meu irmão viuu!! Assim você vai matar o papai. Só digo uma coisa, Domingo ela não vai! Danadaa!! Vem minha odalisca, agora faz essa cobra coral subir!!! Pau que nasce torto, Nunca se endireita. Tchannn!! Tchannn!! Tu du du pááá! Eu gostchu muitchu, heinn! danadinha! Mainhaa! Agora use meu lorem ipsum ordinária!!! Olha o quibeee! rema, rema, ordinária!.",
		u"Você usa o Lorem Ipsum tradicional? Sabe de nada inocente!! Conheça meu lorem que é Tchan, Tchan, Tchannn!! Txu Txu Tu Paaaaa!! Vem, vem ordinária!! Venha provar do meu dendê que você não vai se arrepender. Só na sacanageeem!! Eu gostchu muitchu, heinn! Eitchaaa template cheio de abundância danadaaa!! Assim você mata o papai hein!? Etâaaa Mainhaaaaa...me abusa nesse seu layout, me gera, me geraaaa ordinária!!! Só na sacanagem!!!! Venha provar do meu dendê Tu du du pááá!.",
		u"Mas que abundância meu irmãooo!!! Esse é seu Layout danadaaa!??? Sabe de nada inocente!! Vem, vem, vem ordinária, provar do meu dendê!! Eu gostxuu muitxuu desse seu Layout!! Etâ danadaaaa!! Tá tão lindo que vou falar em inglês só pra você mainhaaa!! Know nothing innocent. Ordinary!! Txhann Txhann, Txu txu tu paaa!! Damned. Only in Slutty!! Abundance that my borther!! Tchan, Tchan, Tchan...Tu tu tu pa!!!!.",
		u"Chama, Chama, Chama ordinária!!!! Tu du du pááá! rema, rema, ordinária! olha o quibe! eu gostchu muitchu, heinn! ordinária!! Domingo ela não vai. Tchannn!! Tchannn!! danadinha! Mainhaa! Eiiitaaa Mainhaaa!! Assim você mata o papai , viuu!! Danadaa!! Vem, vem ordinária!! Ahh mainhaa!! venha provar do meu dendê. Só na sacanageeem!! Sabe de nada inocente! que abundânciaaaa meu irmão!! Pau que nasce torto, Nunca se endireita....",
		u"Vem minha odalisca, agora faz essa cobra coral subir!!! que abundânciaaaa meu irmão!! Sabe de nada inocente! Só na sacanageeem!! venha provar do meu dendê. Ahh mainhaa!! Vem, vem ordinária!! Danadaa!! Assim você mata o papai , viuu!! Eiiitaaa Mainhaaa!! danadinha! Mainhaa! Tchannn!! Tchannn!! Domingo ela não vai. Sunday she won't go!! ordinária!! eu gostchu muitchu, heinn! olha o quibe! rema, rema, ordinária! Tu du du pááá!.",
		u"Agora sim Mainhaaa!!! Me preencha nesse seu layout danadaaa!! Etâaaa mainhaaa!! danadaaa! Tu tu tu paa!!! Mas que abundância meu irmãooo!!! Esse é seu Layout danadaaa!??? Sabe de nada inocente!! Vem, vem, vem ordinária, provar do meu dendê!! Eu gostxuu muitxuu desse seu Layout!! Assim você mata o papai , viuu!! Eiiitaaa Mainhaaa!! danadinha! Mainhaa! Tchannn!! Tchannn!! Domingo ela não vai. Sunday she won't go!! ordinária!! ."
	]

	def generate_para(self, last_word):
		para_return = ""
		region = ""

		# if digit compadre*n, generate a multiple paragraph
		if re.search("compadre(\*\d{1})$", last_word):
			digit = int(re.search("\d{1}?", last_word).group(0))

			if digit <= len(self.__para):
				for i in range(0, digit):
					para_return += self.__para[i]

					if i + 1 != digit:
						para_return += "\n\n"

		# if digit only compadre, generate a single paragraph
		if re.search("compadre$", last_word):
			para_return = self.__para[0]
			
		return para_return


class CompadreIpsumCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		compadre = CompadreIpsum()

		para_return = ""
		region = ""
		cursor_position = self.view.sel()[0].begin()
		last_word = self.view.substr(sublime.Region(cursor_position - 10, cursor_position))

		para_return = compadre.generate_para(last_word)

		if re.search("compadre(\*\d{1})$", last_word):
			region = sublime.Region(cursor_position - 10, cursor_position)

		if re.search("compadre$", last_word):
			region = sublime.Region(cursor_position - 8, cursor_position)

		if para_return != "":
			self.view.replace(edit, region, para_return)


class CompadreIpsumComplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		compadre = CompadreIpsum()

		if re.search("compadre$", prefix):
			completions = []
			complete = ''

			for x in range(1, 7):
				str_idx = str(x)
				key = 'Compadre Ipsum - ' + str_idx

				if x > 1:
					key += ' paragraphs'
				else:
					key += ' paragraph'

				complete = (key, compadre.generate_para('compadre*' + str_idx))
				completions.append(complete)

			return completions
