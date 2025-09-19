describe('Teste E2E de Login', () => {
    it('Visita página e verifica título', () => {
      cy.visit('https://example.com');
      cy.title().should('include', 'Example Domain');
    });
  });