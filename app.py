from flask import Flask, render_template, redirect, session, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "sua_chave_secreta_aqui"

uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)


class Inscricao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_especialista = db.Column(db.String(120), nullable=False)
    data_avaliacao = db.Column(
        db.Date, nullable=False, default=datetime.utcnow().date()
    )
    codigo_cafe = db.Column(db.String(120), nullable=False)
    fragrancia = db.Column(db.Float, nullable=False)
    aroma = db.Column(db.Float, nullable=False)
    docura = db.Column(db.Float, nullable=False)
    corpo = db.Column(db.Float, nullable=False)
    acidez_intensidade = db.Column(db.Float, nullable=False)
    acidez_qualidade = db.Column(db.Float, nullable=False)
    amargor = db.Column(db.Float, nullable=False)
    adstringencia = db.Column(db.Float, nullable=False)
    defeitos = db.Column(db.Float, nullable=False)
    sabor_residual = db.Column(db.Float, nullable=False)
    intensidade = db.Column(db.Float, nullable=False)
    comentarios = db.Column(db.Text)
    # Colunas para os descritores
    alcoolico = db.Column(db.Integer)
    amadeirado = db.Column(db.Integer)
    amendoado_castanha = db.Column(db.Integer)
    animalico = db.Column(db.Integer)
    azedo = db.Column(db.Integer)
    baunilha = db.Column(db.Integer)
    borracha = db.Column(db.Integer)
    caramelizado = db.Column(db.Integer)
    cereal = db.Column(db.Integer)
    chocolate = db.Column(db.Integer)
    cozido = db.Column(db.Integer)
    especiarias = db.Column(db.Integer)
    fermentado = db.Column(db.Integer)
    floral = db.Column(db.Integer)
    frutado = db.Column(db.Integer)
    iodoformio_quimico = db.Column(db.Integer)
    madeira_papelao = db.Column(db.Integer)
    mel = db.Column(db.Integer)
    queimado_defumado = db.Column(db.Integer)
    terroso_mofo = db.Column(db.Integer)
    tostado = db.Column(db.Integer)
    vegetal = db.Column(db.Integer)
    envelhecido_oxidado = db.Column(db.Integer)
    verde_herbaceo = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "nome_especialista": self.nome_especialista,
            "data_avaliacao": self.data_avaliacao.isoformat(),
            "codigo_cafe": self.codigo_cafe,
            "fragrancia": self.fragrancia,
            "aroma": self.aroma,
            "docura": self.docura,
            "corpo": self.corpo,
            "acidez_intensidade": self.acidez_intensidade,
            "acidez_qualidade": self.acidez_qualidade,
            "amargor": self.amargor,
            "adstringencia": self.adstringencia,
            "defeitos": self.defeitos,
            "sabor_residual": self.sabor_residual,
            "intensidade": self.intensidade,
            "comentarios": self.comentarios,
            # Adicionando descritores
            "alcoolico": self.alcoolico,
            "amadeirado": self.amadeirado,
            "amendoado_castanha": self.amendoado_castanha,
            "animalico": self.animalico,
            "azedo": self.azedo,
            "baunilha": self.baunilha,
            "borracha": self.borracha,
            "caramelizado": self.caramelizado,
            "cereal": self.cereal,
            "chocolate": self.chocolate,
            "cozido": self.cozido,
            "especiarias": self.especiarias,
            "fermentado": self.fermentado,
            "floral": self.floral,
            "frutado": self.frutado,
            "iodofórmio_químico": self.iodoformio_quimico,
            "madeira_papelão": self.madeira_papelao,
            "mel": self.mel,
            "queimado_defumado": self.queimado_defumado,
            "terroso_mofo": self.terroso_mofo,
            "tostado": self.tostado,
            "vegetal": self.vegetal,
            "envelhecido_oxidado": self.envelhecido_oxidado,
            "verde_herbáceo": self.verde_herbaceo,
        }


@app.route("/inscricoes")
def inscricoes():
    nome_especialista = session.get("nome_completo")
    if nome_especialista is None:
        return redirect(url_for("home"))

    inscricoes = Inscricao.query.filter_by(nome_especialista=nome_especialista).all()
    return render_template(
        "inscricoes.html", inscricoes=inscricoes, nome_especialista=nome_especialista
    )


def create_tables():
    with app.app_context():
        db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Armazena o nome do usuário na sessão quando o formulário for enviado
        session["nome_completo"] = request.form["nome"]
        return redirect(url_for("home"))

    # Verifica se o nome do usuário já está na sessão e passa essa informação para o template
    nome_completo = session.get("nome_completo", None)
    return render_template("index.html", nome_completo=nome_completo)


@app.route("/inscrever", methods=["POST"])
def inscrever():
    if request.method == "POST":
        nova_inscricao = Inscricao(
            nome_especialista=request.form.get("nome_especialista"),
            data_avaliacao=datetime.strptime(
                request.form.get("data_avaliacao"), "%Y-%m-%d"
            ).date(),
            codigo_cafe=request.form.get("codigo_cafe"),
            fragrancia=request.form.get("fragrancia"),
            aroma=request.form.get("aroma"),
            docura=request.form.get("docura"),
            corpo=request.form.get("corpo"),
            acidez_intensidade=request.form.get("acidez_intensidade"),
            acidez_qualidade=request.form.get("acidez_qualidade"),
            amargor=request.form.get("amargor"),
            adstringencia=request.form.get("adstringencia"),
            defeitos=request.form.get("defeitos"),
            sabor_residual=request.form.get("sabor_residual"),
            intensidade=request.form.get("intensidade"),
            comentarios=request.form.get("comentarios"),
            # Recebendo valores dos descritores
            alcoolico=request.form.get("alcoolico"),
            amadeirado=request.form.get("amadeirado"),
            amendoado_castanha=request.form.get("amendoado_castanha"),
            animalico=request.form.get("animalico"),
            azedo=request.form.get("azedo"),
            baunilha=request.form.get("baunilha"),
            borracha=request.form.get("borracha"),
            caramelizado=request.form.get("caramelizado"),
            cereal=request.form.get("cereal"),
            chocolate=request.form.get("chocolate"),
            cozido=request.form.get("cozido"),
            especiarias=request.form.get("especiarias"),
            fermentado=request.form.get("fermentado"),
            floral=request.form.get("floral"),
            frutado=request.form.get("frutado"),
            iodoformio_quimico=request.form.get("iodoformio_quimico"),
            madeira_papelao=request.form.get("madeira_papelao"),
            mel=request.form.get("mel"),
            queimado_defumado=request.form.get("queimado_defumado"),
            terroso_mofo=request.form.get("terroso_mofo"),
            tostado=request.form.get("tostado"),
            vegetal=request.form.get("vegetal"),
            envelhecido_oxidado=request.form.get("envelhecido_oxidado"),
            verde_herbaceo=request.form.get("verde_herbaceo"),
        )

        db.session.add(nova_inscricao)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("inscrever.html")


@app.route("/limpar_sessao")
def limpar_sessao():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
