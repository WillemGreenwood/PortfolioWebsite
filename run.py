import app as appModule

app = appModule.create_app('config.Config')

if __name__ == "__main__":
    app.run()
