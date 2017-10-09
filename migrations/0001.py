# This migration does the intial database setup

import models

def forward ():
    models.DB.create_tables([models.BlogPost, models.Author])

if __name__ == '__main__':

    forward()
