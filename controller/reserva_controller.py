from models.reserva_model import Reserva
from database import db
from flask import jsonify
import requests

def validar_turma(turma_id):
    try:
        resp = requests.get(f"http://localhost:5050/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException:
        return False

def criar_reserva(data):
    turma_id = data.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=data.get("sala"),
        data=data.get("data"),
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
        } for r in reservas
    ])

def buscar_reserva_por_id(reserva_id):
    reserva = Reserva.query.get(reserva_id)

    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    return jsonify({
        "id": reserva.id,
        "turma_id": reserva.turma_id,
        "sala": reserva.sala,
        "data": reserva.data
    }), 200

def deletar_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)

    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404
    
    db.session.delete(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva deletada com sucesso"}), 200