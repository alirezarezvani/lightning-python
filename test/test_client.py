from lightning import Lightning, Session, Visualization
from random import randrange, uniform
from numpy import random


lightning = Lightning()
lightning.host = 'http://localhost:3000'


class TestLightningAPIClient:

    def test_create_session(self):
        
        session = lightning.create_session()
        
        assert isinstance(session, Session)


    def test_create_named_session(self):
        
        session_name = 'test-session'
        session = lightning.create_session(session_name)
        
        assert isinstance(session, Session)
        assert hasattr(session, 'name')
        assert session.name == session_name


    def test_create_scatter(self):

        x = [randrange(100) for x in xrange(50)]
        y = [randrange(100) for y in xrange(50)]

        viz = lightning.scatter(x, y)

        assert isinstance(viz, Visualization)
        assert hasattr(viz, 'id')


    def test_create_line(self):

        x = [randrange(100) for x in xrange(50)]

        viz = lightning.plot('line', data=x)

        assert isinstance(viz, Visualization)
        assert hasattr(viz, 'id')



    def test_create_image(self):

        img1 = random.rand(256, 256)
        img2 = random.rand(256, 256)

        viz = lightning.image([img1, img2], type='gallery')

        assert isinstance(viz, Visualization)
        assert hasattr(viz, 'id')



    def test_create_roi(self):        


        points = [{ 'x': randrange(100), 'y': randrange(100), 'i': i} for i in xrange(50)]
        timeseries = [[uniform(-1, 1) for _ in xrange(1000)] for _ in xrange(50)]

        data = {
            'points': points,
            'timeseries': timeseries
        }

        viz = lightning.plot(data=data, type='roi')

        assert isinstance(viz, Visualization)
        assert hasattr(viz, 'id')