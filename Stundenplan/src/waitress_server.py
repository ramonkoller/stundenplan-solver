from waitress import serve
import Server_Solver
serve(Server_Solver.app, host='0.0.0.0', port=5000)