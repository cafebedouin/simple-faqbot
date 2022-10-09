# BUYING
def faq_buying(modifier=""):
	if modifier=="ergo":
		df = """
[KYC]
Huobi: <https://www.huobi.com/exchange/erg_usdt/>
GateIO: <https://www.gate.io/trade/ERG_USDT>
Indodax: <https://indodax.com/market/ERGIDR>
HotBit: <https://www.hotbit.io/exchange?symbol=ERG_BTC>
FMFW: <https://fmfw.io/erg-to-btc>
Changelly: <https://changelly.com/exchange/erg>
swopfi: <https://swop.fi/info/3PGVJvV8Ep1u7qMkvUs1DYhRyfvArdRbMsD>

[non-KYC]
KuCoin: <https://www.kucoin.com/trade/ERG-USDT>
CoinEx: <https://www.coinex.com/exchange?currency=usdt&dest=erg>
TradeOgre: <https://tradeogre.com/exchange/BTC-ERG>
		"""
	elif modifier=="ido":
		df = """
Initial decentralized exchange offerings (IDOs) can have as many as three rounds. The first round is a stakers round that is sold at a discounted price to Ergopad stakers who reach a tier. The minimum tier is 12,500 staked Ergopad tokens. The second round is the seed round, and it is open to anyone on a first come, first served basis with a maximum purchase ceiling and higher price than the first round. If there is demand for a third round, then a strategic round is offered with both a higher purchase limit and higher price, but the price is still below the initial IDO price offered on the exchange.
		"""
	else:
		df = """
Ergopad tokens and tokens launched with Ergopad are available for purchase on Spectrum. <https://app.spectrum.fi/ergo/swap>

Modifiers: `ergo`, `ido`
		"""
	return(df)

# CONSOLIDATE
def faq_consolidate():
	df = """
Trouble staking, unstaking, redeeming or contributing? Please send the tokens or key(s), plus erg to yourself in one tx. This will consolidate the tokens & your erg into one utxo. Then retry your (un)stake/redeem/contribution tx. Let @theta_decay know if your tx does not work after consolidation. Thank you.
	"""
	return(df)

# DATES
def faq_dates():
	df = """
You will find relavant dates here: https://www.ergopad.io/projects
	"""
	return(df)

# FEE 
def faq_fee():
	df = """
Do you have enough erg for the tx fee? Having 0.3 erg or more in the same account is recommended.
	"""
	return(df)

# PROBLEM
def faq_problem(modifier=""):
	if modifier=="staking":
		df = """
Please send the tokens you wish to stake, plus a few erg to yourself in one transaction (tx) to consolidate the tokens & your erg into one utxo. Then retry your staking tx. Please let Ergopad community manager @theta_decay know if you have anymore trouble after doing this consolidation. Thank you.
		"""
	elif modifier=="dashboard":
		df = """
If the dashboard is not showing the correct amounts, please check to make sure that all your assets are in the same address in your wallet (a wallet can have multiple addresses), and then try refreshing the website.
		"""
	else:
		df = """
If you are having trouble with staking, unstaking, signing-up for an IDO or have another problem, please contact the community manager, @theta_decay.

Modifiers: `staking`, `dashboard`
		"""
	return(df)

# TIPBOT
def faq_tipbot(modifier=""):
	if modifier=="dis":
		df = """
		To initialize a Discord wallet, message /start to @Ergo Tipper Bot[BETA]#0902.
		"""
	elif modifier=="reddit":
		df = """
		To initialize a Reddit wallet. message !start to /u/ErgoTipperBot.
		"""
	elif modifier=="tg":
		df = """
		To initialize a Telegram wallet, message /start to @ergotipperbot.
		"""
	elif modifier=="twitter":
		df = """
		To initalize a Twitter wallet, message !start to @ErgoTipperBot.
		"""
	else:
		df = """
		Ergo's Tipper Bot can be setup on Discord, Reddit, Telegram and Twitter. You can initialize a tip wallet by messaging the tipbot on each platform.

Platform | Message | Bot Name
=============================
Discord  | /start  | @Ergo Tipper Bot[BETA]#0902
Reddit   | !start  | ErgoTipperBot
Telegram | /start  | @ergotipperbot
Twitter  | !start  | @ErgoTipperBot

Pro-Tip: If you restore the same wallet into each service, you can use the same tip wallet across platforms.

Modifiers: `dis`, `reddit`, `tg`, `twitter`
		"""
	return(df)

# WELCOME
def faq_welcome():
	df = """
Ergopad is a token launch platform for the Ergo blockchain. Ergopad gives investors an opportunity to get in on the ground floor with Ergo tokens offered through an initial decentralized exchanged offering (IDO) . We help projects with our project launch and staking platform, provide developer expertise, and help projects get the resources they need.

Useful links:
Ergpad Website: For more information. <https://www.ergopad.io/>
Ergopad Dashboard: Provides an overview of your wallet. <https://www.ergopad.io/dashboard>
Ergopad FAQ: Frequently Asked Questions <https://www.ergopad.io/faq>
Ergopad White Paper: Description of how Ergopad works. <https://www.ergopad.io/whitepaper>
	"""
	return(df)