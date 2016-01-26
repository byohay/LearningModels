from evolvability.with_population.HGT.HGT_process import HGTProcess

__author__ = 'yben_000'


class HGTProcessConstantGenesNumber(HGTProcess):
    def __init__(self, HGT_factor, length, number_of_genes):
        super(HGTProcessConstantGenesNumber, self).__init__(HGT_factor, length)
        self.number_of_genes = number_of_genes

    def get_number_of_genes_transferring(self):
        return self.number_of_genes
