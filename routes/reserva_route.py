from flask import Blueprint, request
from controller.reserva_controller import criar_reserva, listar_reservas, deletar_reserva, buscar_reserva_por_id

routes = Blueprint("routes", __name__)


@routes.route("/reservas", methods=["POST"])
def post_reserva():
    return criar_reserva(request.json)


@routes.route("/reservas", methods=["GET"])
def get_reservas():
    return listar_reservas()

@routes.route('/reservas/<int:reserva_id>', methods=['DELETE'])
def excluir_reserva(reserva_id):
    return deletar_reserva(reserva_id)

@routes.route('/reservas/<int:reserva_id>', methods=['GET'])
def obter_reserva(reserva_id):
    return buscar_reserva_por_id(reserva_id)
