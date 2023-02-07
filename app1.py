pip install flask

#LA PROCEDURA DETTAGLIATA DELLA PRIMA CONFIGURAZIONE DETTAGLIATA è SPIEGATA NEL FILE DI TESTO ALLEGATO NEL REPOSITORY: APP IN FLASK.DOCX 
contenente codice commentato e spiegato partendo dalla creazione di ogni singola componente. 



from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

#Salvate le modifiche ed eseguite app.py

python app.py

#Creazione di una Home Page

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Python Flask Bucket List App</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                    <li role="presentation"><a href="#">Sign In</a>
                    </li>
                    <li role="presentation"><a href="showSignUp">Sign Up</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Python Flask App</h3>
        </div>
        <div class="jumbotron">
            <h1>Bucket List App</h1>
            <p class="lead"></p>
            <p><a class="btn btn-lg btn-success" href="showSignUp" role="button">Sign up today</a>
            </p>
        </div>
        <div class="row marketing">
            <div class="col-lg-6">
                <h4>Bucket List</h4>
                <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>
                <h4>Bucket List</h4>
                <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>
                <h4>Bucket List</h4>
                <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
            </div>
            <div class="col-lg-6">
                <h4>Bucket List</h4>
                <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>
                <h4>Bucket List</h4>
                <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>
                <h4>Bucket List</h4>
                <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
            </div>
        </div>
        <footer class="footer">
            <p>&copy; Company 2015</p>
        </footer>
    </div>
</body>
</html>

#Aprite app.py ed importate render_template, che utilizzeremo per visualizzare i file del modello.


from flask import Flask, render_template


#Modificate il metodo principale affinchè restituisca il file template. 


def main():
    return render_template('index.html')
