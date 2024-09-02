from flask import Blueprint, request, jsonify,render_template
from . import db
from .models import Trade, Cargo, Inventory, Event

bp = Blueprint('api', __name__)

@bp.route('/api/trades', methods=['POST'])
def initiate_trade():
    data = request.json
    new_trade = Trade(
        id=data['trade_id'],
        buyer=data['buyer'],
        seller=data['seller'],
        item=data['item'],
        quantity=data['quantity'],
        status=data['status'],
        timestamp=data['timestamp']
    )
    db.session.add(new_trade)
    db.session.commit()
    return jsonify({"message": "Trade initiated"}), 201

@bp.route('/api/cargo/<shipment_id>', methods=['GET'])
def get_cargo(shipment_id):
    cargo = Cargo.query.get_or_404(shipment_id)
    return jsonify({
        'shipment_id': cargo.id,
        'description': cargo.description,
        'origin': cargo.origin,
        'destination': cargo.destination,
        'status': cargo.status,
        'expected_delivery': cargo.expected_delivery
    })

@bp.route('/api/inventory/<station_id>', methods=['GET'])
def get_inventory(station_id):
    inventory = Inventory.query.filter_by(station_id=station_id).all()
    inventory_list = [{'item_id': inv.item_id, 'quantity': inv.quantity, 'last_updated': inv.last_updated} for inv in inventory]
    return jsonify(inventory_list)


bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/updates/real-time')
def real_time_updates():
    # Replace this with actual data retrieval logic
    trade_data = {
        'tradeLabels': ['Planet A', 'Planet B', 'Planet C'],
        'tradeVolumes': [100, 150, 200],
        'inventoryLabels': ['Station X', 'Station Y', 'Station Z'],
        'inventoryLevels': [500, 400, 300]
    }
    return jsonify(trade_data)