################################################################################
## RPC-client connection information (required)
################################################################################
#host   = "localhost" # Not required
#port   = 8092        # .. because linked via docker
#user   = ""          # Not required
#passwd = ""          # .. because secure connection within docker containers

################################################################################
## Wallet passphrase
################################################################################
unlock = ""

################################################################################
## Delegate Feed Publish Parameters
################################################################################
delegate_name            = "init0"
maxAgeFeedInSeconds      = 60*60 # 1hour

################################################################################
## Fine tuning
################################################################################
discount                     = 0.995  # discoun for shorts
core_exchange_factor         = 0.95   # 5% discount if paying fees in bitassets
maintenance_collateral_ratio = 1750   # Call when collateral only pays off 175% the debt
maximum_short_squeeze_ratio  = 1100   # Stop calling when collateral only pays off 110% of the debt
change_min                   = 0.5    # Percentage of price change to force an update
minValidAssetPriceInBTC      = 0.00001# minimum valid price for BTS in BTC

## Enable exchanges
enable_yunbi             = True
enable_btc38             = True
enable_bter              = False
enable_poloniex          = True
enable_bittrex           = True
enable_btcavg            = True

## trust level for exchanges (if an exception happens and level is 0.8 script
##                            will quit with a failure)
btc38_trust_level        = 0.9
bter_trust_level         = 0.5
poloniex_trust_level     = 1.0
bittrex_trust_level      = 0.5
yunbi_trust_level        = 0.8

ask_confirmation = False
