from client import AgenticMicropaymentEscrowSettlementGatewayClient

def main():
    client = AgenticMicropaymentEscrowSettlementGatewayClient()
    res = client.lock_agent_escrow_settlement('0x123...abc', '0x456...def', 25.00)
    print('Agent Micropayment Gateway: ' + res['escrow_tx_id'] + ' (State: ' + res['escrow_state'] + ')')
    print('Amount: $' + str(res['authorized_amount_usd']) + ' | Fee: $' + str(res['estimated_gas_or_settlement_fee_usd']))
    print('Receipt Hash: ' + res['cryptographic_receipt_hash'])
    print('Explorer URL: ' + res['onchain_settlement_explorer_url'])

if __name__ == '__main__':
    main()
